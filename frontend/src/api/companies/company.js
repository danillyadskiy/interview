import Service from '../service'

const resource = '/company';


export default {
  list() {
    return Service.get(`${resource}`);
  },
}
