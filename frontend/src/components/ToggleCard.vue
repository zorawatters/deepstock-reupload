<template>
  <div :class = "custom" @click="setCompany">
    <!-- <p>{{ticker}} - {{name}} <t> <a style="color:28a745"> {{high}} </a>|<a style="color:dc3545"> {{low}} </a></p> -->
    <div class="">
      <b-row>
        <div class="col-8 card ">
          <b-row>
            <div class="card-body p-2 m-1 ">
              <h6 style = "color:#42b983; align:right" class="card-title">{{ticker}}</h6>
              [
              <a class="text-success">321</a><a style="padding-left:.25em "></a>
              <a style="padding-right:.25em "></a>

              |

              <a style="padding-left:.25em "></a>
              <a class="text-danger">123</a>
              ]
              <!-- <p class="card-text">INSERT TWEET HERE</p>
              <a href="#" class="btn btn-primary">Link to tweet/bio?</a> -->
            </div>
            <div class="card-footer text-muted">
              {{metadata.shortName}} the name of the company
            </div>

          </b-row>
        </div>
        <div class="col-4">
          <img :src="metadata.logo_url" width = "60" height = "60" class="rounded-circle">
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
    setCompany:function(){
      this.$store.commit('setTicker', this.ticker)
    }
  },
  async mounted(){
    var tick = '/'
    tick = tick + this.ticker
    this.metadata = (await this.$http(this.$backendUrl + tick +'/metadata')).data
  }
}
</script>
