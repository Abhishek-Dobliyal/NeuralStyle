<template>
  <div class="position-fixed bottom-0 end-0 p-3" style="z-index: 11">
      <div
        id="liveToast"
        ref="liveToastDiv"
        class="toast"
        role="alert"
        aria-live="assertive"
        aria-atomic="true"
      >
        <div class="toast-header">
          <i :class="`fa ${toastIconClass} fa-2x px-1`" :style="`color: ${toastIconColor};`"/>
          <strong class="me-auto">{{ title }}</strong>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="toast"
            aria-label="Close"
          ></button>
        </div>
        <div class="toast-body">{{ bodyMessage }}</div>
      </div>
    </div>
</template>

<script>
export default {
    name: "LiveToast",
    props: {
        title: String,
        bodyMessage: String,
        toastIconClass: String,
        toastIconColor: String
    }
}
</script>

<style>

</style>