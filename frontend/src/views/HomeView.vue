<template>
  <div class="container">
    <Header :heading="this.headerHeading" :subHeading="this.headerSubHeading" />
    <div class="d-flex my-5 justify-content-between">
      <ImageInput imgLabel="Upload Content Image" :inputType="true" />
      <ImageInput imgLabel="Upload Style Image" :inputType="false" />
    </div>
    <div class="row g-3 mt-3">
      <div class="col-md">
        <Slider
          sliderTitle="Epochs"
          sliderType="1"
          :minValue="5"
          :maxValue="30"
          :steps="5"
          :initialValue="10"
        />
      </div>
      <div class="col-md">
        <Slider
          sliderTitle="Content Weight"
          sliderType="2"
          :minValue="1"
          :maxValue="10"
          :steps="0.5"
          :initialValue="3"
        />
      </div>
      <div class="col-md">
        <Slider
          sliderTitle="Style Weight"
          sliderType="3"
          :minValue="1"
          :maxValue="7"
          :steps="0.5"
          :initialValue="2"
        />
      </div>
    </div>
    <Button buttonText="Process & Style" />
  </div>
</template>

<script>
import Header from "@/components/Header.vue";
import ImageInput from "@/components/ImageInput.vue";
import Button from "@/components/Button.vue";
import Slider from "@/components/Slider.vue";

export default {
  name: "HomeView",
  components: {
    Header,
    ImageInput,
    Button,
    Slider,
  },
  data() {
    return {
      headerHeading: "NeuralStyle",
      headerSubHeading: "Style your snaps with the power of Deep Learning",
    };
  },
};
</script>
