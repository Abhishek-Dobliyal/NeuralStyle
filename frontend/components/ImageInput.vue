<template>
  <div class="container mt-5">
    <div class="row">
      <div class="col-lg-9 mx-auto">
        <!-- Upload image input-->
        <div class="input-group mb-3 px-2 py-2 rounded-pill bg-white shadow-lg">
          <input
            id="upload"
            @change="readURL"
            type="file"
            class="form-control border-0"
          />
          <label
            id="upload-label"
            for="upload"
            class="text-muted"
            >{{ imageLabel }}</label
          >
          <div class="input-group-append">
            <label for="upload" class="btn btn-light m-0 rounded-pill px-3">
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
            :src="selectedImage"
            alt=""
            class="img-fluid rounded shadow-sm mx-auto d-block"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ImageInput",
  data() {
      return {
          selectedImage: "",
          imageLabel: "Upload",
      }
  },
  methods: {
    readURL(input) {
      let file = input.target.files;
      if (file && file[0]) {
        this.imageLabel = file[0].name;

        let reader = new FileReader();
        reader.onload = (event) => {
          this.selectedImage = event.target.result;
        };
        reader.readAsDataURL(file[0]);
      }
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
  border: 2px dashed #52514e;
  padding: 1rem;
  position: relative;
}

.image-area::before {
  content: "Preview";
  color: #52514e;
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
