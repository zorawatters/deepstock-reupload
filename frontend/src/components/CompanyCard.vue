<template>
<div :class = "custom">
<h3 class="section-description">About </h3>
<div class="section-description">{{metadata.longBusinessSummary }} </div>
<div class="grid-4"></div>
<div class="info"><h4 class="Employees">Employees</h4><div class="space"></div>
<div class="result"> {{metadata.fullTimeEmployees }} </div></div>
<div class="info"><h4 class="Headquarters"> Headquarters </h4><div class="space"></div>
<div class="result"> {{metadata.city}}, {{metadata.state}} </div></div>
<div class="info"><h4 class="Market"> Market Cap</h4><div class="space"></div>
<div class="result"> {{fundamentals ? fundamentals.marketCap.fmt : ''}} </div></div>
<div class="info"><h4 class="Average"> Average Volume </h4><div class="space"></div>
<div class="result"> {{fundamentals ? fundamentals.averageVolume.fmt : ''}} </div></div>
<div class="info"><h4 class="52WeekHigh "> 52 Week High </h4><div class="space"></div>
<div class="result"> {{fundamentals ? fundamentals.fiftyTwoWeekHigh.fmt : ''}} </div></div>
<div class="info"><h4 class="52WeekLow"> 52 Week Low </h4><div class="space"></div>
<div class="result"> {{fundamentals ? fundamentals.fiftyTwoWeekLow.fmt : ''}} </div></div>

</div>
</template>
<script>
export default {
  name: 'company-card',
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
      fundamentals : {
      }
    }
  },
  async mounted(){
    var tick = '/'
    tick = tick + this.ticker
    this.metadata = (await this.$http(this.$backendUrl + tick +'/metadata')).data
    this.fundamentals = (await this.$http(this.$backendUrl + tick +'/fundamentals')).data
  }
}
</script>