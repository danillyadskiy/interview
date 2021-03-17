<template>
  <v-container class="mt-5" >
      <v-row no-gutters>
        <v-col cols="1">
          <v-btn
              class="btn-search"
              text
              icon
              v-on:click="searchCompany">
            <v-icon>mdi-magnify</v-icon>
          </v-btn>
        </v-col>
        <v-col cols="10">

          <!-- Строка поиска -->
          <v-text-field
              outlined
              placeholder="Введите название компании или региона"
              v-model="keyWordSearch"
              v-on:keyup.enter="searchCompany"
          ></v-text-field>

          <!-- Карточка компании -->
          <v-expansion-panels multiple v-if="companies">
            <v-expansion-panel
                v-for="company in companies"
                :key="company.name"
            >
              <v-expansion-panel-header>
                <v-row>
                  <v-col cols="12" md="4" v-html="highlight(company.name)"></v-col>
                  <v-col cols="12" md="8" v-html="highlight(company.region)"></v-col>
                </v-row>
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-divider></v-divider>
                <v-row class="mt-4" no-gutters >
                  <v-col cols="12" md="4">
                    <v-row align="center">
                      <v-col cols="12" sm="3">ИНН</v-col>
                      <v-col cols="12" sm="8">{{ company.inn }}</v-col>
                    </v-row>
                    <v-row align="center">
                      <v-col cols="12" sm="3">КПП</v-col>
                      <v-col cols="12" sm="8">{{ company.kpp }}</v-col>
                    </v-row>
                    <v-row align="center" v-if="company.registration_date">
                      <v-col cols="12" sm="3" md="11" xl="3">дата регистрации</v-col>
                      <v-col cols="12" sm="8">{{ company.registration_date }}</v-col>
                    </v-row>
                    <v-row align="center">
                      <v-col cols="12" sm="3" md="11" xl="3">ОКОПФ</v-col>
                      <v-col cols="12" sm="8" md="11" xl="8">{{ company.okopf }}</v-col>
                    </v-row>
                    <v-row align="center" no-gutters v-if="company.email">
                      <v-col cols="3">email</v-col>
                      <v-col cols="8">
                        <v-btn icon :href="'mailto:' + company.email">
                          <v-icon>mdi-email</v-icon>
                        </v-btn>
                      </v-col>
                    </v-row>
                    <v-row align="center" no-gutters v-if="company.link">
                      <v-col cols="3">сайт</v-col>
                      <v-col cols="8">
                        <v-btn
                            icon
                            :href="company.link"
                            target="_blank"
                            rel="noopener noreferrer">
                          <v-icon>mdi-link</v-icon>
                        </v-btn>
                      </v-col>
                    </v-row>
                  </v-col>
                  <v-col cols="12" md="8" v-if="company.main_okved">
                    <v-row align="center">
                      <v-col cols="1">ОКВЭД</v-col>
                    </v-row>
                    <v-row align="center" no-gutters>
                      <v-col cols="12" md="2" xl="1">{{ company.main_okved }}</v-col>
                      <v-col cols="12" md="10" xl="11">{{ company.main_okved_name }}</v-col>
                    </v-row>
                    <v-row
                        align="center"
                        no-gutters
                        class="okved"
                        v-for="okved in sortOkvedASC(company.okved)"
                        :key="okved.code"
                    >
                      <v-col cols="12" md="2" xl="1">{{ okved.code }}</v-col>
                      <v-col cols="12" md="10" xl="11">{{ okved.name }}</v-col>
                    </v-row>
                  </v-col>
                </v-row>
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>

          <!-- Результат поиска отсутствует -->
          <div class="text-center" v-if="isCompaniesEmpty">
            Ничего не найдено!
          </div>

        </v-col>
        <v-col cols="1">
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
      isCompaniesEmpty: false,
      keyWordSearch: this.$route.query.q || ''
    }
  },
  mounted() {
      this.searchCompany()
  },
  methods: {
    searchCompany: function () {
      if (this.keyWordSearch) {
        // Замена параметра в строке запроса в соотвествии с ключевым словом поиска
        this.$router.replace({ query: {q: this.keyWordSearch} }).catch(() => {});
        // Запрос к API, запись и проверка на наличие результатов
        api.get({q: this.keyWordSearch})
            .then(response => {
              this.companies = response.data;
              this.isCompaniesEmpty = !response.data.length;
            });
      }
    },
    sortOkvedASC: function(arr) {
      // Использован slice(), чтобы избежать бесконечного цикла
      return arr.slice().sort(function(a, b) {
        return a.code - b.code;
      });
    },
    highlight(text) {
      // Флаг 'g' - чувствительный к регистру
      const check = new RegExp(this.keyWordSearch, 'g');
      return text.replace(check,'<span class="highlighted">$&</span>');
    }
  }
}
</script>

<style scoped>
.btn-search {
  float: right;
  margin-top: 10px;
  margin-right: 5px;
}
.okved {
  color: #9e9e9e;
}
::v-deep .highlighted {
  color: #3575cf;
}
</style>