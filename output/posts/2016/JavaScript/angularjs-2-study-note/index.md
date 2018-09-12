.. title: AngularJS 2 Study Note (Continually Update)
.. date: 2016-08-16
.. category: JavaScript
.. tags: AngularJS, draft
.. slug: angularjs-2-study-note
.. authors: Pengyin Shan

While my recent project involving in processing data, I think this is a good chance for to touch AngularJS 2, and a little bit TypeScript. *This study note follows BASICS and DEVELOPER GUIDE part in official document*.

<!-- TEASER_END -->



#Reference List

- <a href="https://angular.cn">AngularJS 2 Official Website (Chinese)</a>

- <a href="https://angular.io/">AngularJS 2 Office Website (English)</a>

#Architecture

Based on official suggestion, an angular app should contains following parts:

- HTML Templates: combined with Angular-markup/tags

- Component: talk directly with templates through property binding and event binding.

- Injectable Service: creating business logic. It talk with components, but not with template.

- Modules: boxing components and injectable services.

Other parts includes MetaData, Directives, etc. Angular website has a very clear graph which describe how things works together:

img-responsive images/articles/2016/javascript/angular-architecture.png 

#Module

Angular Module is also called `NgModule`.

Generally, module is used to:

1. divide components, directives and pipes into cohesive blocks of functionality.

2. Add services to application. These services can be loaded immediately or use lazy-loading.

All modules are a `class` with **decorator** called `@NgModule`.

It includes **root module** and **feature module**, which includes a group of similar domain or business logic. Root module will **import** feature modules to use them.


>A **decorator** is used to add `metadata` to class, like `@randomly` or `@superhero`.

##AppModule

Every angular app has a **root module**, called `AppModule`. It is in `app.module.ts` file.

The minimal `app.module.ts`:

    :::typescript
    import { NgModule }      from '@angular/core';
    import { BrowserModule } from '@angular/platform-browser';

    //This imports setting in app.component.ts
    import
           { AppComponent }  from './app.component';

    @NgModule({
      imports: [ BrowserModule ],
      declarations: [ AppComponent ],
      bootstrap:    [ AppComponent ]
    })
    export class AppModule { }

`app.component.ts`:

    :::typescript
    import { Component } from '@angular/core';

    @Component({
      selector: 'my-app',
      template: '<h1>{{title}}</h1>',
    })
    //This class is exported and being imported in app.module.ts
    export class AppComponent {
      title = 'Minimal NgModule';
    }

Bootstrap process can be done dynamically or statically. Official document has detail.

##NgModule

NgModule is a decorator class. It has following properties:

- `declarations`: the **view classes** that belong to this module. Angular has three kinds of view classes: `components`, `directives` and `pipes`.

- `exports`: the parts for exports can be visible and used in the *component templates* of other modules.

- `imports`: the classes from other modules, which is used by component templates in this module.

- `providers`: provides services. The services created by this provider are usable all around module.

- `bootstrap`: identify main application view. Can only be used set in root module.

Example NgModule:

    :::typescript
    @NgModule({
      imports:      [ BrowserModule ], //BrowserModule is used for run app in browser
      providers:    [ Logger ],
      declarations: [ AppComponent ],
      exports:      [ AppComponent ],
      bootstrap:    [ AppComponent ]
    });

Normally, `main.ts` is used to **bootstrapping** the root module, like following:

    :::typescript
    import { bootstrap } from '@angular/platform-browser-dynamic';
    import { AppComponent } from './app.component';
    import {HTTP_PROVIDERS} from '@angular/http';


    bootstrap(AppComponent, [HTTP_PROVIDERS]);

##Angular Module Library

Angular has a series of module libraries. User can use `import {} from '@angular/XXX` format to import and use it.

Use `npm` to install these modules.