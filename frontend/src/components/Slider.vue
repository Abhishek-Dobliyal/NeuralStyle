<template>
  <div class="container">
    <label for="customRange3" class="form-label">{{ sliderTitle }}</label>
    <input
      type="range"
      class="form-range"
      :min="minValue"
      :max="maxValue"
      :step="steps"
      :value="initialValue"
      @change="sendSliderValue"
    />
  </div>
</template>

<script>
export default {
  name: "Slider",
  props: {
    sliderTitle: String,
    sliderType: String, // 1 for Epoch Slider, 2 for Content Weight Slider, 3 for Style Slider
    minValue: Number,
    maxValue: Number,
    steps: Number,
    initialValue: Number,
  },
  methods: {
    sendSliderValue(event) {
      let sliderDetails = {
        sliderType: this.sliderType,
        sliderValue: event.target.value,
      };
      this.$store.commit("storeSliderValues", sliderDetails);
    },
  },
};
</script>

<style scoped>
  label {
    color: aliceblue;
  }
</style>
