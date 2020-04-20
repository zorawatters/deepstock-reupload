<template>
<div :class = "custom">
  
</div>
</template>
<script>

  export default {
    name: 'twitter-card',
    props: {
      custom: {
        type: String,
        default: ''
      },
      ticker: {
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
