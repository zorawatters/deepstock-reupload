<template>
<div :class = "custom">
  <p>Twitter here </p>
</div>
</template>
<script>

  export default {
    name: 'twitter-card',
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
