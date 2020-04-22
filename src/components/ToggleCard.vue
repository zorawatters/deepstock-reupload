<template>
  <div :class = "custom" @click="setCompany">
    <!-- <p>{{ticker}} - {{name}} <t> <a style="color:28a745"> {{high}} </a>|<a style="color:dc3545"> {{low}} </a></p> -->
    <div class="">
      <b-row>
        <div class="col-8 card shadow opacity:40%">
          <b-row>
            <div class="card-footer ">
              <a style = "color:#42b983; align:right;" class="card-title"><b>{{ticker}}</b></a><br>
              [
              <a class="text-success">${{currentPrice.toFixed(2)}}</a><a style="padding-left:.25em "></a>
              <a style="padding-right:.25em "></a>

              |

              <a style="padding-left:.25em "></a>
              <a class="text-danger">{{percentChange.toFixed(2)}}%</a>
              ]
              <br>
              <a class="text-muted">
              {{metadata.shortName}}
              some sample text here
            </a>
              <!-- <p class="card-text">INSERT TWEET HERE</p>
              <a href="#" class="btn btn-primary">Link to tweet/bio?</a> -->
            </div>
            <div class="card-footer text-muted">

            </div>

          </b-row>
        </div>
        <div class="col-3" style="align-items: center;">
          <img :src="metadata.logo_url" width = "80" height = "80" class="rounded-circle pt-2 pl-2 shadow">
        </div>
      </b-row>
    </div>
  </div>
</template>
<script>
import { mapGetters } from 'vuex';


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
      },
    }
  },
  methods:{
    setCompany:function(){
      this.$store.commit('setTicker', this.ticker)
    }
  },
  async mounted(){
    this.metadata = (await this.$http(this.$backendUrl + '/'+ this.ticker +'/metadata')).data
  },
  computed: {
    ...mapGetters({
      //metadata: 'getMetadata',
      companyInfo: 'getStockData'
    }),
    currentPrice(){
      var cd = this.companyInfo(this.ticker)['chartData']
      if(cd){
        return Number.parseFloat(cd[cd.length-1][1])
      }else{
        return 0
      }
    },
    percentChange(){
      var cd = this.companyInfo(this.ticker)['chartData']
      if(cd){
        var open = Number.parseFloat(cd[0][1])
        return (((this.currentPrice - open) / open))*100
      }
    }
  }
}
</script>
