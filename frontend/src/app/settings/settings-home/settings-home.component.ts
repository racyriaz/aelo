import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'settings-home',
  templateUrl: './settings-home.component.html',
  styleUrls: ['./settings-home.component.scss']
})
export class SettingsHomeComponent implements OnInit {

  constructor() { }

  panelOpenState = false;

  ngOnInit(): void {
  }

}
