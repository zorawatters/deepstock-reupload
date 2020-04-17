<template>
    <div :class="custom">
      <h1>{{title}}</h1>
      <slot></slot>
    </div>
</template>
<script>

export default {
  name: 'main-card',
  props: {
    title: {
      type: String,
      default: ''
    },
    custom:{
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
