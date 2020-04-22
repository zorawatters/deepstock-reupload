<template>
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
