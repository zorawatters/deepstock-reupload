<template>
  <div :class = "custom" @click="setTicker">
    <!-- <p>{{ticker}} - {{name}} <t> <a style="color:28a745"> {{high}} </a>|<a style="color:dc3545"> {{low}} </a></p> -->
    <div class="">
      <b-row>
      <div class="col-8">
        <b-row class="center">
          <a style = "color:dc3545">{{ticker}}</a>
        </b-row>
        <b-row>
          {{metadata.shortName}} the name of the company will go here
        </b-row>
        </div>
        <div class="col-4">
          <img :src="metadata.logo_url" width = "60" height = "60">
        </div>
      </b-row>
      </div>
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
          shortName : '',
          logo_url : '',
          website : ''
        }
      }
    },
    methods:{
      setTicker:function(){
        console.log("ticker")
        this.$store.commit('setTicker', this.ticker)
        console.log("Called")
      }
    },
    async mounted(){
      var tick = '/'
      tick = tick + this.ticker
      this.metadata = (await this.$http(this.$backendUrl + tick +'/metadata')).data
    }
  }
  </script>
