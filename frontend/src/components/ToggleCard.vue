<template>
<div :class = "custom">
  <!-- <p>{{ticker}} - {{name}} <t> <a style="color:28a745"> {{high}} </a>|<a style="color:dc3545"> {{low}} </a></p> -->
    <p> <a style = "color:dc3545">{{ticker}}</a> {{metadata.name}} <img :src="metadata.logoUrl"></p>
</div>
</template>
<script>

  export default {
    name: 'toggle-card',
    props: {
      custom: {
        type: String,
        default: ''
      },

      ticker: {
        type: String,
        default: ''
      },
     
    },
    data(){
      return {
        metadata: {
          name: '',
          logoUrl: ''
        }
      }
    },
    async mounted(){
      this.ticker
      this.metadata = (await this.$http(this.$backendUrl + '/metadata')).data
    }
  }
</script>
