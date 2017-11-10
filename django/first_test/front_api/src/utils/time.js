class TimeFormat {

    getFullTime(long) {
        const DATE =  new Date(long);
        const Y = 1900 + DATE.getYear();
        const Mon = DATE.getMonth() >= 9 ? DATE.getMonth() + 1 : "0" + (DATE.getMonth() + 1);
        const D = DATE.getDate() >= 10 ? DATE.getDate() : "0" + DATE.getDate();
        const H =  DATE.getHours() >= 10 ? DATE.getHours() : "0" + DATE.getHours();
        const Min = DATE.getMinutes() >= 10 ? DATE.getMinutes() : "0" + DATE.getMinutes();
        const S = DATE.getSeconds() >= 10 ? DATE.getSeconds() : "0" + DATE.getSeconds();
        return Y + '-' + Mon + '-' + D + ' ' + H + ':' + Min + ':' + S
    }

}
export default TimeFormat