<template>
    <div class="card shadow">
      <h1>{{title}}</h1>
      <slot></slot>
      <h2>End of content</h2>
    </div>
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
  /* border: 2px dashed black; */
  width:200px;
}
</style>
