<template>
  <v-container class="mt-5" >
      <v-row no-gutters>
        <v-col cols="12" sm="1" md="1">
          <v-btn text icon v-on:click="searchCompany">
            <v-icon>mdi-magnify</v-icon>
          </v-btn>
        </v-col>
        <v-col cols="12" sm="10" md="10">
          <v-text-field
              outlined
              placeholder="Введите название компании или региона"
              v-model="keyWordSearch"
              v-on:keyup.enter="searchCompany"
          ></v-text-field>
        </v-col>
        <v-col cols="12" sm="1" md="1">
        </v-col>
      </v-row>
    </v-container>
</template>

<script>
import api from '@/api/companies/company'

export default {
  name: "CompaniesPage",
  page: {
    title: "Страница поиска компаний"
  },
  data() {
    return {
      companies: [],
      keyWordSearch: this.$route.query.q || ''
    }
  },
  mounted() {
      this.searchCompany()
  },
  methods: {
    searchCompany: function () {
      if (this.keyWordSearch) {
        this.$router.replace({ query: {q: this.keyWordSearch} })
        api.get({q: this.keyWordSearch})
            .then(response => {this.companies = response.data;});
      }
    }
  }
}
</script>

<style scoped>
.v-btn {
  float: right;
  margin-top: 10px;
  margin-right: 5px;
}
</style>