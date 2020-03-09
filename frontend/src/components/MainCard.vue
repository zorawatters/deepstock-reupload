<template>
  <b-row class="shadow-lg p-3 mb-5 bg-white rounded col-sm">
    <b-col>
      <div class="card">
        <h1>{{title}}</h1>
        <slot></slot>
        <h2>End of content</h2>
      </div>
    </b-col>
    <b-col>
    </b-col>

  </b-row>
</template>
<script>

export default {
  name: 'main-card',
  props: {
    title: {
      type: String,
      default: ''
    }
  },
  data(){
    return {
    }
  }
}

</script>
<style scoped>
.card {
  border: 2px dashed black;
  width:
}
</style>
