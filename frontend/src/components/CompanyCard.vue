<template>
  <div :class = "custom">
    <h3 class="card-header">About </h3>
    <b-row>
      <div class = "col-12 text-left list-group list-group-horizontal">
        <b-row class="">
        <dl class="col-6 pt-5">
          <ul>
            <li class="list-group-item"><span class="text-left "><b>Employees</b> <span style="color:#42b983" class="">48016 </span></span></li>
            <!-- Use this one ^^-->
            <!-- <div class="result"> {{metadata.fullTimeEmployees }} </div></div> -->

            <li class="list-group-item"><span class="text-left "><b>Headquarters</b> <span style="color:#42b983" class="">Palo Alto, CA  </span></span></li>
            <!-- Use this one ^^-->
            <!-- <div class="result"> {{metadata.city}}, {{metadata.state}} </div></div> -->


            <li class="list-group-item"><span class="text-left "><b>Market Cap</b> <span style="color:#42b983" class="">126.62B</span></span></li>
            <!-- Use this one ^^-->
            <!-- <div class="result"> {{fundamentals.marketCap.fmt }} </div></div> -->
          </ul>
          </dl>
          <dl class="col-6 pt-5">
            <ul>
            <li class="list-group-item"><span class="text-left "><b>Average Volume</b> <span style="color:#42b983" class="">20.72M </span></span></li>
            <!-- Use this one ^^-->
            <!-- <div class="result"> {{fundamentals.averageVolume.fmt }} </div></div> -->

            <li class="list-group-item"><span class="text-left "><b>52 Week High</b> <span style="color:#42b983" class="">968.99</span></span></li>

          <!-- Use this one ^^-->
          <!-- <div class="result"> {{fundamentals.fiftyTwoWeekHigh.fmt }} </div></div> -->

          <li class="list-group-item"><span class="text-left "><b>52 Week Low</b> <span style="color:#42b983" class="">176.99</span></span></li>

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
          Tesla, Inc. designs, develops, manufactures, leases, and sells electric vehicles, and energy generation and storage systems in the United States, China, Netherlands, Norway, and internationally. The company operates in two segments, Automotive; and Energy Generation and Storage. The Automotive segment offers sedans and sport utility vehicles. It also provides electric powertrain components and systems; and services for electric vehicles through its company-owned service locations, and Tesla mobile service technicians, as well as sells used vehicles. This segment markets and sells its products through a network of company-owned stores and galleries, as well as through its own Website. The Energy Generation and Storage segment offers energy storage products, such as rechargeable lithium-ion battery systems for use in homes, industrial, commercial facilities, and utility grids; and designs, manufactures, installs, maintains, leases, and sells solar energy generation and energy storage products to residential and commercial customers. It also provides vehicle insurance services, as well as renewable energy. The company was formerly known as Tesla Motors, Inc. and changed its name to Tesla, Inc. in February 2017. Tesla, Inc. was founded in 2003 and is headquartered in Palo Alto, California.
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
