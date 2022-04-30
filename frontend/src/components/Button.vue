<template>
  <div class="container my-4">
    <div class="container my-3" v-if="!buttonDisabled">
      <button class="btn btn-outline-warning" @click="sendFiles" ref="sendBtn">
        {{ buttonText }}
      </button>
    </div>

    <div class="container my-3" v-else>
      <button class="btn btn-outline-warning" type="button" disabled>
        <span
          class="spinner-border spinner-border-sm mx-2"
          role="status"
          aria-hidden="true"
        ></span>
        Please wait...
      </button>
    </div>
    <LiveToast
        :title="toastTitle"
        :bodyMessage="toastMessage"
        :toastIconClass="toastIconClass"
        :toastIconColor="toastIconColor"
        ref="liveToast"
      />
  </div>
</template>

<script>
import LiveToast from "@/components/LiveToast.vue";

export default {
  name: "Button",
  components: {
    LiveToast,
  },
  props: {
    buttonText: String,
  },
  data() {
    return {
      toastTitle: "",
      toastMessage: "",
      toastIconClass: "",
      toastIconColor: "",
      isButtonDisabled: false,
    };
  },
  computed: {
    buttonDisabled() {
      return this.isButtonDisabled;
    },
  },
  methods: {
    isBothImagesSelected() {
      return (
        this.$store.getters.getContentImage !== null &&
        this.$store.getters.getStyleImage !== null
      );
    },
    sendFiles() {
      if (!this.isBothImagesSelected()) {
        this.toastTitle = "Oops...";
        this.toastMessage = "Kindly select both the images!";
        this.toastIconClass = "fa fa-exclamation-circle";
        this.toastIconColor = "red";
        let toastDiv = this.$refs.liveToast.$refs.liveToastDiv; // Accessing LiveToast Component $refs
        let toast = new bootstrap.Toast(toastDiv);
        toast.show();
      } else {
        this.isButtonDisabled = true;
        this.toastTitle = "Success!";
        this.toastMessage =
          "Your images will be sent to the server for processing. This might take a while...";
        this.toastIconClass = "fa fa-check-circle";
        this.toastIconColor = "green";
        let toastDiv = this.$refs.liveToast.$refs.liveToastDiv; // Accessing LiveToast Component $refs
        let toast = new bootstrap.Toast(toastDiv);
        toast.show();
        this.$store
          .dispatch("postImages")
          .then((res) => {
            this.$store.commit("setModelLoss", res.data);
            this.$router.push("result");
          })
          .catch((err) => {
            console.log(err);
          });
      }
    },
  },
};
</script>
