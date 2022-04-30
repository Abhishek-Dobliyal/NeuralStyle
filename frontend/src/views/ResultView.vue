<template>
  <div class="container">
    <div class="spinner-container container" v-if="!isFileReady">
      <div
        class="spinner-grow text-warning text-center"
        style="width: 4rem; height: 4rem"
        role="status"
      ></div>
      <div class="container text-center mt-3 mx-2">
        <span class="lead text-warning">Please Wait! Fetching Results...</span>
      </div>
    </div>
    <div class="container" v-else>
      <Header heading="Stylized" subHeading="Results" />
      <div class="container w-50">
        <div class="image-area mt-5">
          <img
            id="imageResult"
            :src="receivedImage"
            alt=""
            class="img-fluid rounded shadow-lg mx-auto d-block"
          />
        </div>
      </div>
      <div class="container my-4 w-75">
        <div class="row g-2">
          <div class="col">
            <a
              class="btn btn-outline-success"
              download="stylized.jpg"
              :href="receivedImage"
              @click="showDownloadToast"
              >Download</a
            >
          </div>
          <div class="col">
            <button class="btn btn-outline-info" @click="$router.push('/')">
              Style Again
            </button>
          </div>
          <div class="col">
            <button class="btn btn-outline-danger" @click="displayModelParams">
              {{ modelParamBtnText }}
            </button>
          </div>
        </div>
      </div>
      <div class="container my-3 w-50" v-if="showParamList">
        <span class="lead my-2 text-warning">Model Parameters</span>
        <ul
          class="list-group list-group-flush"
          v-for="(paramValue, paramName) in modelParams"
        >
          <li class="list-group-item">{{ paramName }} : {{ paramValue }}</li>
        </ul>
      </div>
      <LiveToast
        :title="toastTitle"
        :bodyMessage="toastMessage"
        :toastIconClass="toastIconClass"
        :toastIconColor="toastIconColor"
        ref="liveToast"
      />
    </div>
  </div>
</template>

<script>
import Header from "@/components/Header.vue";
import LiveToast from "@/components/LiveToast.vue";

export default {
  name: "ResultView",
  components: {
    Header,
    LiveToast,
  },
  data() {
    return {
      receivedImage: "",
      isFileReceived: false,
      modelParams: {},
      showParamList: false,
      modelParamBtnText: "Show Model Params",
      toastTitle: "",
      toastMessage: "",
      toastIconClass: "",
      toastIconColor: "",
    };
  },
  computed: {
    isFileReady() {
      setTimeout(() => {
        this.showResultToast();
      }, 200);
      return this.isFileReceived;
    },
  },
  mounted() {
    this.$store.dispatch("getResult");
    setTimeout(() => {
      if (this.$store.getters.getReceivedImage !== null) {
        let modelParameters = {};
        let sliderValues = this.$store.getters.getSliderValues;
        let modelLoss = this.$store.getters.getModelLoss;
        modelParameters["loss"] = modelLoss;
        Object.keys(sliderValues).forEach((key) => {
          modelParameters[key] = sliderValues[key];
        });
        this.modelParams = modelParameters;
        this.isFileReceived = true;
        this.receivedImage = this.$store.getters.getReceivedImage;
      }
    }, 1000);
  },
  methods: {
    displayModelParams() {
      if (this.showParamList) {
        this.showParamList = false;
        this.modelParamBtnText = "Show Model Params";
      } else {
        this.showParamList = true;
        this.modelParamBtnText = "Hide Model Params";
      }
    },
    showResultToast() {
      this.toastTitle = "Style Transfer Complete!";
      this.toastMessage = "Your image has been successfully stylized.";
      this.toastIconClass = "fa fa-check-circle";
      this.toastIconColor = "green";
      let toastDiv = this.$refs.liveToast.$refs.liveToastDiv; // Accessing LiveToast Component $refs
      let toast = new bootstrap.Toast(toastDiv);
      toast.show();
    },
    showDownloadToast() {
      this.toastTitle = "Image Downloaded!";
      this.toastMessage = "Your image has been downloaded.";
      this.toastIconClass = "fa fa-arrow-down";
      this.toastIconColor = "steelblue";
      let toastDiv = this.$refs.liveToast.$refs.liveToastDiv; // Accessing LiveToast Component $refs
      let toast = new bootstrap.Toast(toastDiv);
      toast.show();
    },
  },
};
</script>

<style scoped>
.spinner-container {
  margin-top: 10rem;
}

.image-area {
  border: 2px dashed whitesmoke;
  padding: 1rem;
  position: relative;
}

.image-area::before {
  color: #777572;
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
