<template>
<div :class = "custom">
  <p>Sentiment here </p>
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
