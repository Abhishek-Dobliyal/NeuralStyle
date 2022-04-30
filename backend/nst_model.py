""" Required Imports """
import tensorflow as tf
import numpy as np
import cv2


CONTENT_LAYER = "block5_conv2"
STYLE_LAYERS = ["block1_conv1", "block2_conv1", "block3_conv1", "block4_conv1", "block5_conv1"]
WEIGHTS_PATH = "./vgg19_weights_tf_dim_ordering_tf_kernels.h5"

"""
Layers in the pre-trained VGG19

['input_1',
 'block1_conv1', => Style Layer
 'block1_conv2',
 'block1_pool',
 'block2_conv1', => Style Layer
 'block2_conv2',
 'block2_pool',
 'block3_conv1', => Style Layer
 'block3_conv2',
 'block3_conv3',
 'block3_conv4',
 'block3_pool',
 'block4_conv1', => Style Layer
 'block4_conv2', => Content Layer
 'block4_conv3',
 'block4_conv4',
 'block4_pool',
 'block5_conv1', => Style Layer
 'block5_conv2',
 'block5_conv3',
 'block5_conv4',
 'block5_pool',]
 """

class NST:

    def __init__(self, content_img_path, style_img_path,
                                epochs=15, style_weight=1e-2, content_weight=1e-3):

        self.epochs = epochs
        self.style_weight = style_weight
        self.content_weight = content_weight

        self.content_img, self.style_img = self.load_images(content_img_path,
                                                                                                                            style_img_path)
        self.vgg_model = self.load_vgg()
        self.optimizer = tf.keras.optimizers.Adam(learning_rate=0.05)
        self.content_target, self.style_target = self.get_target_images()
        self.loss = None


    def get_gram_matrix(self, matrix: tf.Tensor) -> tf.Tensor:
        """
        Takes in an image tensor and computes the gram matrix
        for it.

        Params:
            matrix (tf.Tensor) : An image tensor

        Returns:
            (tf.Tensor) : The computed gram matrix of the input tensor
        """
        numerator = tf.einsum("bijc,bijd->bcd", matrix, matrix)
        numerator_result = tf.expand_dims(numerator, axis=0)
        matrix_shape = tf.shape(matrix)
        denominator = tf.cast(matrix_shape[1] * matrix_shape[2], tf.float32)

        return numerator_result / denominator


    def load_vgg(self) -> tf.keras.Model:
        """
        Loads the pre-trained VGG19 model from tensorflow.keras.applications

        Params:
            None

        Returns:
            (tf.keras.Model) : Pre-trained VGG19 model
        """
        vgg = tf.keras.applications.VGG19(include_top=True, weights=None)
        vgg.load_weights(WEIGHTS_PATH)
        vgg.trainable = False

        content_res = vgg.get_layer(CONTENT_LAYER).output
        style_res = [vgg.get_layer(layer).output for layer in STYLE_LAYERS]
        gram_style_res = [self.get_gram_matrix(output) for output in style_res]

        model = tf.keras.Model([vgg.input], [content_res, gram_style_res])
        print("Model loaded!")
        return model


    def load_images(self, content_img_path: str, style_img_path: str) -> tuple:
        """
        Takes content and style images path and loads them

        Params:
            content_img_path (str) : Content image path
            style_img_path (str) : Style image path

        Returns:
            (tuple) : Both the content and style image representation inside a tuple
        """
        content_image = cv2.resize(cv2.imread(content_img_path), (224, 224))
        content_image = tf.image.convert_image_dtype(content_image, tf.float32)
        style_image = cv2.resize(cv2.imread(style_img_path), (224, 224))
        style_image = tf.image.convert_image_dtype(style_image, tf.float32)
        print("\nImages successfully loaded!")
        return content_image, style_image


    def get_loss(self, style_outputs: tf.Tensor,
                                 style_target: tf.Tensor,
                                 content_outputs: tf.Tensor,
                                 content_target: tf.Tensor) -> float:
        """
        Computes the loss function in terms of style and content loss

        Params:
        style_outputs (tf.Tensor) :
        style_target (tf.Tensor) :
        content_outputs (tf.Tensor) :
        content_target (tf.Tensor) :

        Returns:
            (float) : The total loss

        """
        content_loss = tf.reduce_mean((content_outputs - content_target) ** 2)
        style_loss = tf.add_n(tf.reduce_mean((output - target) ** 2) for output, target in zip(style_outputs, style_target))

        total_loss = (self.style_weight * style_loss) + (self.content_weight * content_loss)
        return total_loss


    def get_target_images(self) -> tuple:
        """
        Loads the VGG model and passes the content and style image
        through it to generate the target images.

        Params:
            None

        Returns:
            (tuple) : Tuple consisting of the target images
        """
        print("Generating output!")

        content_target = self.vgg_model(np.array([self.content_img * 255]))[0]
        style_target = self.vgg_model(np.array([self.style_img * 255]))[1]

        return content_target, style_target


    def apply_gradients(self, image: tf.Tensor, epoch: int) -> None:
        """
        Trains the model for the given number of epochs

        Params:
            image (tf.Tensor) : Image to train model on
            epochs (int) : Number of epochs

        Returns:
            None
        """
        with tf.GradientTape() as tape:
            output = self.vgg_model(image * 255)
            loss = self.get_loss(output[1], self.style_target, output[0], self.content_target)

        gradient = tape.gradient(loss, image)
        self.optimizer.apply_gradients([(gradient, image)])
        image.assign(tf.clip_by_value(image, clip_value_min=0.0, clip_value_max=1.0)) # Important step to avoid dilution of image

        if epoch % 10 == 0:
            print(f"Loss: {loss}. Please wait....",)
            self.loss = float(loss)


    def generate_stylized_img(self) -> np.ndarray:
        """
        Generates the final stylized image

        Params:
            None

        Returns:
            (np.ndarray) : The stylized image array
        """
        image = tf.Variable([self.content_img]) # Make image variable so its pixel values can be changed

        for epoch in range(self.epochs):
            self.apply_gradients(image, epoch)

        image = np.float32(tf.squeeze(image))
        cv2.imwrite("stylized.jpg", image * 255)
        print("Output successfully generated!\n")
        return image
