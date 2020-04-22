<template>
<<<<<<< HEAD
  <div :class = "custom">
    <h3 class="card-header">About </h3>
    <b-row>
      <div class = "col-12 text-left list-group list-group-horizontal">
        <b-row class="">
        <dl class="col-6 pt-5">
          <ul>
            <li class="list-group-item"><span class="text-left "><b>Employees</b> <span style="color:#42b983" class="">{{metadata.fullTimeEmployees }}</span></span></li>
            <!-- Use this one ^^-->
            <!-- <div class="result"> {{metadata.fullTimeEmployees }} </div></div> -->

            <li class="list-group-item"><span class="text-left "><b>Headquarters</b> <span style="color:#42b983" class="">{{metadata.city}}, {{metadata.state}} </span></span></li>
            <!-- Use this one ^^-->
            <!-- <div class="result"> {{metadata.city}}, {{metadata.state}} </div></div> -->


            <li class="list-group-item"><span class="text-left "><b>Market Cap</b> <span style="color:#42b983" class="">{{fundamentals.marketCap.fmt }}</span></span></li>
            <!-- Use this one ^^-->
            <!-- <div class="result"> {{fundamentals.marketCap.fmt }} </div></div> -->
          </ul>
          </dl>
          <dl class="col-6 pt-5">
            <ul>
            <li class="list-group-item"><span class="text-left "><b>Average Volume</b> <span style="color:#42b983" class="">{{fundamentals.averageVolume.fmt }} </span></span></li>
            <!-- Use this one ^^-->
            <!-- <div class="result"> {{fundamentals.averageVolume.fmt }} </div></div> -->

            <li class="list-group-item"><span class="text-left "><b>52 Week High</b> <span style="color:#42b983" class="">{{fundamentals.fiftyTwoWeekHigh.fmt }}</span></span></li>

          <!-- Use this one ^^-->
          <!-- <div class="result"> {{fundamentals.fiftyTwoWeekHigh.fmt }} </div></div> -->

          <li class="list-group-item"><span class="text-left "><b>52 Week Low</b> <span style="color:#42b983" class="">{{fundamentals.fiftyTwoWeekLow.fmt }}</span></span></li>

          <!-- Use this one ^^-->
          <!-- <div class="result"> {{fundamentals.fiftyTwoWeekLow.fmt }} </div></div> -->
        </ul>
        </dl>
      </b-row>
      </div>
    </b-row>
    <b-row>
      <div class = "col-12 pl-4 pr-4 ">
        <p class = "text-left text-muted h6 card p-4">
          {{metadata.longBusinessSummary }}
        </p>
        <!-- Use this one ^^-->
        <!-- <div class="section-description">{{metadata.longBusinessSummary }} </div> -->
      </div>
    </b-row>

  </div>
=======
<div :class = "custom">
<h3 class="section-description">About </h3>
<div class="section-description">{{metadata ? metadata.longBusinessSummary : ''}} </div>
<div class="grid-4"></div>
<div class="info"><h4 class="Employees">Employees</h4><div class="space"></div>
<div class="result"> {{metadata ? metadata.fullTimeEmployees : ''}} </div></div>
<div class="info"><h4 class="Headquarters"> Headquarters </h4><div class="space"></div>
<div class="result"> {{metadata ? metadata.city : ''}}, {{metadata ? metadata.state : ''}} </div></div>
<div class="info"><h4 class="Market"> Market Cap</h4><div class="space"></div>
<div class="result"> {{fundamentals && fundamentals.marketCap ? fundamentals.marketCap.fmt : ''}} </div></div>
<div class="info"><h4 class="Average"> Average Volume </h4><div class="space"></div>
<div class="result"> {{fundamentals && fundamentals.averageVolume ? fundamentals.averageVolume.fmt : ''}} </div></div>
<div class="info"><h4 class="52WeekHigh "> 52 Week High </h4><div class="space"></div>
<div class="result"> {{fundamentals && fundamentals.fiftyTwoWeekHigh ? fundamentals.fiftyTwoWeekHigh.fmt : ''}} </div></div>
<div class="info"><h4 class="52WeekLow"> 52 Week Low </h4><div class="space"></div>
<div class="result"> {{fundamentals && fundamentals.fiftyTwoWeekLow ? fundamentals.fiftyTwoWeekLow.fmt : ''}} </div></div>

</div>
>>>>>>> a485fb473c64d78d59511ad64619c8c0892c005d
</template>
<script>
import {mapGetters} from 'vuex'
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
      // metadata: {
      //   longBusinessSummary : '',
      //   fullTimeEmployees : '',
      //   city : '',
      //   state: '',

      // },
      // fundamentals : {
      //   marketCap: {fmt: ''},
      //   averageVolume: {fmt: ''},
      //   fiftyTwoWeekLow: {fmt: ''},
      //   fiftyTwoWeekHigh: {fmt: ''}
      // }
    }
  },
  async mounted(){
    var tick = '/'
    tick = tick + this.ticker
    //this.metadata = (await this.$http(this.$backendUrl + tick +'/metadata')).data
    //this.fundamentals = (await this.$http(this.$backendUrl + tick +'/fundamentals')).data
  },
  computed: mapGetters({
    metadata: 'getMetadata',
    fundamentals: 'getFundamentals'
  })
}
</script>
