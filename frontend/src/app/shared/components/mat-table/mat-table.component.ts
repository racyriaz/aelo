import { CookieService } from 'ngx-cookie-service';
import { HttpClient } from '@angular/common/http';
import { AfterViewInit, Component, ViewChild } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';

@Component({
  selector: 'material-table',
  templateUrl: './mat-table.component.html',
  styleUrls: ['./mat-table.component.scss']
})
export class MatTableComponent implements AfterViewInit {
  displayedColumns: string[] = ['type_of_trans', 'amount', 'cat_of_trans', 'trans_date', 'trans_hour', 'id', 'payment_mode', 'user'];
  dataSource!: MatTableDataSource<$TableElement>;
  username: string;
  constructor(private http: HttpClient, private cookie: CookieService) {
    this.username = this.cookie.get('username');
    this.http.get<Array<$TableElement>>(`http://localhost:8000/history/?username=${this.username}`).subscribe(
      (val) => {
        this.dataSource = new MatTableDataSource<$TableElement>(val);
        this.dataSource.paginator = this.paginator;

      }
    );
  }

  @ViewChild(MatPaginator) paginator!: MatPaginator;
  ngAfterViewInit() {
  }
}

export interface $TableElement {
  type_of_trans: string;
  amount: string;
  cat_of_trans: string;
  trans_date: string;
  trans_hour: string;
  id: string;
  payment_mode: string;
  user?: string;
}

// const ELEMENT_DATA: TableElement[] = [

//   {
//     id: "f32b1014-bb7a-4a01-87f4-78e9fc502b55", amount: "12.000", type_of_trans: "debit", cat_of_trans: "healthy", trans_date: "2021-08-08", trans_hour: "8", payment_mode: "cash", user: "riaz"
//   },
//   {
//     type: false, amount: 2153, category: "food", date: "2021-02-25", time: "12:45"
//   },
//   {
//     type: true, amount: 6212, category: "food", date: "2021-02-25", time: "12:45"
//   },
//   {
//     type: false, amount: 800, category: "food", date: "2021-02-25", time: "12:45"
//   },
//   {
//     type: true, amount: 14, category: "food", date: "2021-02-25", time: "12:45"
//   },
// ];