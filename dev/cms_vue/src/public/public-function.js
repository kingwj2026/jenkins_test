// eslint-disable-next-line no-unused-vars
import { post } from '@/lin/plugins/axios'

const PUBLIC = {
  async httpRequest(url, info, cb) {
    let data = null
    // eslint-disable-next-line no-undef
    await axios.post(url, `data=${JSON.stringify(info)}&message=&serviceStamp=0`, {
      timeout: 300000,
      headers: {
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
      },
    }).then(res => {
      if (this.checkResult(res)) {
        if (cb) {
          // eslint-disable-next-line prefer-destructuring
          data = res.data
          cb(data)
        }
      }
    })
  },
  checkResult(res) {
    if (res.error_code === 0) {
      return true
    } else {
      alert(res.msg)
    }
    return false
  }

}

export default PUBLIC
