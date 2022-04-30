<template>
  <div class="container mt-5">
    <div class="row">
      <div class="col-lg-9 mx-auto">
        <!-- Upload image input-->
        <div class="input-group mb-3 px-2 py-2 rounded-pill bg-white shadow-lg">
          <input
            id="upload"
            @change="onFileSelected"
            ref="fileInput"
            type="file"
            class="form-control border-0"
          />
          <label id="upload-label" for="upload" class="text-muted">{{
            imageLabel
          }}</label>
          <div class="input-group-append" @click="$refs.fileInput.click()">
            <label for="" class="btn btn-light m-0 rounded-pill px-3">
              <i class="fa fa-upload mr-2 text-muted"></i
              ><small class="text-uppercase font-weight-bold text-muted"
                >Choose</small
              ></label
            >
          </div>
        </div>
        <div class="image-area mt-5">
          <img
            id="imageResult"
            :src="getPreviewImage"
            alt=""
            class="img-fluid rounded shadow-lg mx-auto d-block"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ImageInput",
  props: {
    imgLabel: String, // Image name to display in the label tag when an image is selected 
    inputType: Boolean, // true for Content Image, false for Style Image
  },
  data() {
    return {
      imageLabel: this.imgLabel
    }
  },
  computed: {
    getPreviewImage() {
      return this.inputType
        ? this.$store.getters.getContentImage
        : this.$store.getters.getStyleImage;
    },
  },
  methods: {
    onFileSelected(event) {
      let fileDetails = event.target.files
      this.imageLabel = fileDetails[0].name;
      let details = { inputType: this.inputType, file: fileDetails };
      this.$store.commit("onFileSelected", details);
    },
  },
};
</script>

<style scoped>
#upload {
  opacity: 0;
}

#upload-label {
  position: absolute;
  top: 50%;
  left: 1rem;
  transform: translateY(-50%);
}

.image-area {
  border: 2px dashed whitesmoke;
  padding: 1rem;
  position: relative;
}

.image-area::before {
  content: "Preview";
  color: whitesmoke;
  font-weight: bold;
  text-transform: uppercase;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 0.8rem;
  z-index: 1;
}

.image-area img {
  z-index: 2;
  position: relative;
}
</style>
