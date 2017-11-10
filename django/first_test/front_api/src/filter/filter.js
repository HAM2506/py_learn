import Time from '../utils/time.js'
const T = new Time()

export default {
    filterObj: {
        time: (value) => {
            if (!value) return ''
            return T.getFullTime(value)
        }
    }
}