<template>
  <div class="container mt-3">
        <h3 class="display-4">{{ heading }}</h3>
        <span id="subheading" class="h4"> {{ subHeading }}</span>
  </div>
</template>

<script>
export default {
    name: "Header",
    props: {
        heading: String,
        subHeading: String,
    }
}
</script>