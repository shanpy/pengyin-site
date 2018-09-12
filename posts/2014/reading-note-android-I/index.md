.. title: Reading Note for Andorid Development Guide Part I
.. date: 2015-01-13
.. modified: 2015-06-02
.. category: Others
.. tags: Android, Java
.. slug: reading-note-android-I
.. authors: Pengyin Shan
.. description: This post is transferred from my <a href="http://blogpengyin.herokuapp.com/">old Hexo blog site</a>, created on late 2014. This post contains my notes when I was reading Android development guide from Goolge Developer website.

#Android Intents and Intent Filters from Developer Guides

http://developer.android.com/guide/components/intents-filters.html

An Intent is a messaging object you can use to request an action from another app component.

Intent carries information for determining which object to start

Information that the recipient component uses in order to properly perform the action

Start a new instance of an Activity by passing an Intent to `startActivity()`.

Receieve result from activity by calling `startActivityForResult()`.

Bind a service to another component by passing an Intent to `bindService()`.

Deliver a broadcast by passing an Intent to `sendBroadcast()`, `sendOrderedBroadcast()` or `sendStickyBroadcast()`.

Two types of intents:

Explicit intents: used to start a component inside app. Must know class name or service name before start

Always use explicit intent when starting a service and do not declare intent filter for service:

    :::java
    // Executed in an Activity, so 'this' is the context
    // The fileUrl is a string Url, such as "http://www.example.com/image.png"
    Intent downloadIntent = new Intent(this, DownloadService, class);
    downloadIntent.setData(Uri.parse(fileUrl));
    startService(downloadIntent);

An explicit intent is always delivered to its target, regardless of any intent filters the componenet declares.

Implicit intents: don't specify class name. declare an action and ask other app to perform it.

To start implicit intents, the intent defined in `intent filter` in `manifest file` will be find and match with passed intent. If matching, system start another app/component and deliver the passed intenet:

    :::java
    //Create the text message with a string
    Intent sendIntent = new Intent();
    sendIntent.setAction(Intent.ACTION_SEND);
    sendIntent.putExtra(Intent.EXTRA_TEXT, textMessage);
    sendIntent.setType(HTTP.PLAIN_TEXT_TYPE);
    // "text/plain" MIME Type
    //Verify that the intent will resolve to an activity, in case no app in device can start this activity
    if (sendIntent.resolveActivity(getPackageManager()!=null)){
        startActivity(sendIntent);
    }

Intent filter is an expression in manifest file to search for components that should receive the intent.

Intent has following information:

- Componenet Name: must have for explict (ex. service) and skipped for implict

- Example Name: `com.example.ExActivity`

- Set component name: `setComponent()`, `setClass()`, `setClassName()` or `Intent constructor`

Action: a string that specifies the generic action to perform (such as view or pick)

>Example: `ACTION_VIEW`: use for `startActivity()`. Activity should show something to user, like picture

> - Example: `ACTION_SEND`: i.e. "share"intent. use for `startActivity()`. Activity should have data to share with other apps, like email.

    :::java
    static final String ACTION_TIME = "com.example.action.TIME"

Data: A URI object that references data to be acted and/or the MIME type of data.

content: URI will specify MIME type of data

`setData()`: set data URI. `setType()`: set MIME type. `setDataAndType()`: set both data and type

`setDate()` and `setType()` can not be used at the same time: null problem

Catagory: optional. Describe info about the kind of component that should handle the intent. Andorid will know which app should start based on this

>Example: `CATEGORY_BROWSABLE`: target the activity that start a web browser and show data referenced by a link

>Example: `CATAGORY_LAUNCHER`: tartget the activity that initial a task and listed in system's application launcher

Extras: *Key-Value* pair that carry additional information.  using `putExtra()` or create Bundle

>Example: define recipts or subjects in am email-send action

Flags: define metadata for intent. use `setFlags()`.

Forcing an app choose:

    :::java
    Intent intent = new Intent(Intent.ACTION_SEND);
    //...
    //Always use string resource for UI text
    //This says something like "Share this photo with"
    String title = getResources.getString(R.string.chooser_title);
    //Create intent to show chooser
    Intent chooser = Intent.createChooser(intent, title);
    //This is used to call app chooser
    //Verify the intent will resolve at least one activity
    if (intent.resolveActivity(getPackageManager()) != null){
        startActivity(intent);
    }

Receiving an Implicit Intent:

The system will deliver an implicit intent to app only if the intent pass through one of intent filters.

Each unique job should have a intent filter

Inside `<intent-filter>`:

- `<action>`: declares the intent action accepted, in the name attribute. Value must be a literal string.

- `<data>`: declares the type of data accepted, using attributes from data URL (scheme, host, port, path, etc) and MIME type.

- `<category>`: declares the intent category accepted, in the name attribute and value must be literal string.

Example:

    :::xml
    <activity android:name="ShareActivity">
        <intent-filter>
            <action android:name="android.intent.action.SEND"/>
            <catagory android:name="android.intent.category.DEFAULT"/>
            <data android:mimeType="text/plain"/>
        </intent-filter>
    </activity>

Pending Intent: a wrapper around an Intent object. Purpose is to get permission to a foreign application to use the contained intent

Cases to use it:
- Declare an intent to be executed when the user performs an action with your *notification* /Notification Manager Execution
-
- Declare an intent to be executed when the user performs an action with your *App Widget* /Home Screen App Execution



