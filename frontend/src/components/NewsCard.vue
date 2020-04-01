<template>
<div :class = "custom">
  <p>News Articles here </p>
</div>
</template>
<script>

  export default {
    name: 'news-card',
    props: {
      custom: {
        type: String,
        default: ''
      },
    },
    data(){
      return {
      }
    }
  }
</script>
