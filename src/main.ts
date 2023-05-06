import 'zone.js/dist/zone';
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { bootstrapApplication } from '@angular/platform-browser';

declare var cloudinary: any;

@Component({
  selector: 'my-app',
  standalone: true,
  imports: [CommonModule],
  template: `
  <h1>
  Welcome to Here
  </h1>
  <div id="media-library-container"></div>
  `,
})
export class App implements OnInit {
  ngOnInit(): void {
    var timeStamp = Math.round(+new Date() / 1000);

    (<any>window).myML = cloudinary.openMediaLibrary(
      {
        cloud_name: 'marysedespaignet',
        api_key: '519277133588862',
        username: 'adespaignet@gmail.com',
        timestamp: timeStamp,
        inline_container: '#media-library-container',
        multiple: true,
        max_files: 8,
      },
      {
        insertHandler: function (data: { assets: any[] }) {
          data.assets.forEach((asset) => {
            console.log('Inserted asset:', JSON.stringify(asset, null, 2));
          });
        },
      }
    );
  }
}

bootstrapApplication(App);
