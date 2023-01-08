import { createStore } from "vuex";
import axios from "axios";
import { Buffer } from "buffer";

const processImagesURL = "https://neural-style-backend.onrender.com/process";
const getResultURL = "https://neural-style-backend.onrender.com/result";

const headers = {
  "Content-Type": "multipart/form-data",
};

export default createStore({
  state: {
    contentImageFile: null,
    styleImageFile: null,
    contentPreviewImg: null,
    stylePreviewImg: null,
    contentImageName: "",
    styleImageName: "",
    sliderValues: {
      epochs: 2,
      contentWeight: 0.01,
      styleWeight: 0.001,
    },
    receivedImage: null,
    receivedModelLoss: 0.0,
  },
  getters: {
    getContentImage(state) {
      return state.contentPreviewImg;
    },
    getStyleImage(state) {
      return state.stylePreviewImg;
    },
    getContentFileName(state) {
      return state.contentImageName;
    },
    getStyleFileName(state) {
      return state.styleImageName;
    },
    getContentFile(state) {
      return state.contentImageFile;
    },
    getStyleFile(state) {
      return state.styleImageFile;
    },
    getSliderValues(state) {
      return state.sliderValues;
    },
    getReceivedImage(state) {
      return state.receivedImage;
    },
    getModelLoss(state) {
      return state.receivedModelLoss;
    },
  },
  mutations: {
    onFileSelected(state, payload) {
      let file = payload.file;

      if (file && file[0]) {
        let reader = new FileReader();
        reader.onload = (event) => {
          if (payload.inputType) {
            state.contentImageName = file[0].name;
            state.contentPreviewImg = event.target.result;
            state.contentImageFile = file[0];
          } else {
            state.styleImageName = file[0].name;
            state.stylePreviewImg = event.target.result;
            state.styleImageFile = file[0];
          }
        };
        reader.readAsDataURL(file[0]);
      }
    },

    storeSliderValues(state, sliderDetails) {
      let sliderValue = sliderDetails.sliderValue;
      let sliderType = sliderDetails.sliderType;

      switch (sliderType) {
        case "1":
          state.sliderValues.epochs = parseInt(sliderValue);
          break;
        case "2":
          state.sliderValues.contentWeight = sliderValue / 100;
          break;
        case "3":
          state.sliderValues.styleWeight = sliderValue / 100;
          break;
      }
      console.log(state.sliderValues);
    },

    setReceivedImage(state, payload) {
      state.receivedImage = payload;
    },

    setModelLoss(state, payload) {
      state.receivedModelLoss = payload.loss;
    },
  },
  actions: {
    async postImages(context) {
      let formData = new FormData();
      let contentImgBlob = new Blob([context.getters.getContentFile]);
      let styleImgBlob = new Blob([context.getters.getStyleFile]);
      formData.append(
        "contentImage",
        contentImgBlob,
        context.getters.getContentFileName
      );
      formData.append(
        "styleImage",
        styleImgBlob,
        context.getters.getStyleFileName
      );
      // Append Slider values to the form data
      let currentSliderValues = context.getters.getSliderValues;
      Object.keys(currentSliderValues).forEach((key) => {
        formData.append(key, currentSliderValues[key]);
      });

      let uploadStatusPromise = await axios.post(
        processImagesURL,
        formData,
        headers,
        { timeout: 5 }
      );
      return uploadStatusPromise;
    },

    async getResult(context) {
      let receivedResponse = await axios.get(getResultURL, {
        responseType: "arraybuffer",
      });
      let receivedImageBase64 = Buffer.from(
        receivedResponse.data,
        "binary"
      ).toString("base64");
      receivedImageBase64 = "data:image/jpg;base64," + receivedImageBase64;
      context.commit("setReceivedImage", receivedImageBase64);
    },
  },
  modules: {},
});
