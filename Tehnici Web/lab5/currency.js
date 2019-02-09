const am = '';

window.addEventListener('load', () => {
  let app = new Vue({
    el: '#app',
    data: {
      curr: [],
      Data: null,
      EUR: null,
      USD: null
    },
    created: function () {
      //aici vrem sa incarcam dinamic de pe internet
      let data = this; //pt ca dupa this se duce in XMLHttpRequest
      let x = new XMLHttpRequest();
      x.onreadystatechange = function () {
        //console.log(this.readyState); // ca sa verificam ca merge
        if (this.readyState == 4 && this.status == 200) { //200 e ok in limbaj http
          //console.log(this.responseText); // ca sa verificam ca merge
          let arr = [];
          let csv = this.responseText;
          //spargem liniile
          let rows = csv.split('\n');
          //console.log(rows);
          let props = [];
          for (let i in rows) {
            let cells = rows[i].split(',');
            if (i == 0) {
              props = cells;
            }
            else {
              let obj = {};
              for (let c in cells) {
                obj[props[c]] = cells[c];
              }
              arr.push(obj);
            }
          }
          //console.log(arr);
          data.curr = arr;
        }
      }

      x.open('GET', 'https://play.trixbits.ro/data/currency.csv');
      x.send();
    },
    methods: {
      ADD: function () {
        let obj = {
          Data: this.Data,
          EUR: this.EUR,
          USD: this.USD
        }
        this.curr.push(obj);
      },
      EDIT: function (i) {
        this.Data = this.curr[i].Data;
        this.EUR = this.curr[i].EUR;
        this.USD = this.curr[i].USD;
      },
      REMOVE: function (i) {
        this.curr.splice(i, 1);
      },
    },
  });
}
)