<template>
<div :class = "custom">
  <p>Stock graph here </p>
</div>
</template>
<script>

  export default {
    name: 'stock-card',
    props: {
      custom: {
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
