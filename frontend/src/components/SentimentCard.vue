<template>
<div :class = "custom">
  <b>Sentiment Analysis:</b>
  <p style="color:red">The world is falling apart...</p>
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
