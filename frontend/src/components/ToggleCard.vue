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
              <a class="text-success">${{currentPrice.toFixed(2)}}</a><a style="padding-left:.25em "></a>
              <a style="padding-right:.25em "></a>

              |

              <a style="padding-left:.25em "></a>
              <a class="text-danger">{{percentChange.toFixed(2)}}%</a>
              ]
              <!-- <p class="card-text">INSERT TWEET HERE</p>
              <a href="#" class="btn btn-primary">Link to tweet/bio?</a> -->
            </div>
            <div class="card-footer text-muted">
              {{metadata.shortName}}
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
      chartData: []
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
      //var cd = this.companyInfo(this.ticker)['chartData']
      var cd = this.chartData
      if(cd && cd.length > 0){
        return Number.parseFloat(cd[cd.length-1][1])
      }else{
        return 0
      }
    },
    percentChange(){
      //var cd = this.companyInfo(this.ticker)['chartData']
      var cd = this.chartData
      if(cd && cd.length > 0){
        var open = Number.parseFloat(cd[0][1])
        return (((this.currentPrice - open) / open))*100
      }else{
        return 0
      }
    }
  },
  watch: {
    companyInfo: {
      deep: true,
      handler(val){
        this.chartData = val(this.ticker)['chartData']
      }
    }
  }
}
</script>
