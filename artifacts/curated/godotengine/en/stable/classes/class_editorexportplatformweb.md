# EditorExportPlatformWeb

Inherits: EditorExportPlatform < RefCounted < Object

Exporter for the Web.

## Description

The Web exporter customizes how a web build is handled. In the editor's
"Export" window, it is created when adding a new "Web" preset.

Note: Godot on Web is rendered inside a `<canvas>` tag. Normally, the canvas
cannot be positioned or resized manually, but otherwise acts as the main
Window of the application.

## Tutorials

  * Exporting for the Web

  * Web documentation index

## Properties

String | custom_template/debug  
---|---  
String | custom_template/release  
int | html/canvas_resize_policy  
String | html/custom_html_shell  
bool | html/experimental_virtual_keyboard  
bool | html/export_icon  
bool | html/focus_canvas_on_start  
String | html/head_include  
Color | progressive_web_app/background_color  
int | progressive_web_app/display  
bool | progressive_web_app/enabled  
bool | progressive_web_app/ensure_cross_origin_isolation_headers  
String | progressive_web_app/icon_144x144  
String | progressive_web_app/icon_180x180  
String | progressive_web_app/icon_512x512  
String | progressive_web_app/offline_page  
int | progressive_web_app/orientation  
bool | variant/extensions_support  
bool | variant/thread_support  
bool | vram_texture_compression/for_desktop  
bool | vram_texture_compression/for_mobile  
  
## Property Descriptions

String custom_template/debug

File path to the custom export template used for debug builds. If left empty,
the default template is used.

String custom_template/release

File path to the custom export template used for release builds. If left
empty, the default template is used.

int html/canvas_resize_policy

Determines how the canvas should be resized by Godot.

  * None: The canvas is not automatically resized.

  * Project: The size of the canvas is dependent on the ProjectSettings.

  * Adaptive: The canvas is automatically resized to fit as much of the web page as possible.

String html/custom_html_shell

The custom HTML page that wraps the exported web build. If left empty, the
default HTML shell is used.

For more information, see the Customizing HTML5 Shell tutorial.

bool html/experimental_virtual_keyboard

Experimental: This property may be changed or removed in future versions.

If `true`, embeds support for a virtual keyboard into the web page, which is
shown when necessary on touchscreen devices.

bool html/export_icon

If `true`, the project icon will be used as the favicon for this application's
web page.

bool html/focus_canvas_on_start

If `true`, the canvas will be focused as soon as the application is loaded, if
the browser window is already in focus.

String html/head_include

Additional HTML tags to include inside the `<head>`, such as `<meta>` tags.

Note: You do not need to add a `<title>` tag, as it is automatically included
based on the project's name.

Color progressive_web_app/background_color

The background color used behind the web application.

int progressive_web_app/display

The display mode to use for this progressive web application. Different
browsers and platforms may not behave the same.

  * Fullscreen: Displays the app in fullscreen and hides all of the browser's UI elements.

  * Standalone: Displays the app in a separate window and hides all of the browser's UI elements.

  * Minimal UI: Displays the app in a separate window and only shows the browser's UI elements for navigation.

  * Browser: Displays the app as a normal web page.

bool progressive_web_app/enabled

If `true`, turns this web build into a progressive web application (PWA).

bool progressive_web_app/ensure_cross_origin_isolation_headers

When enabled, the progressive web app will make sure that each request has
cross-origin isolation headers (COEP/COOP).

This can simplify the setup to serve the exported game.

String progressive_web_app/icon_144x144

File path to the smallest icon for this web application. If not defined,
defaults to the project icon.

Note: If the icon is not 144144, it will be automatically resized for the
final build.

String progressive_web_app/icon_180x180

File path to the small icon for this web application. If not defined, defaults
to the project icon.

Note: If the icon is not 180180, it will be automatically resized for the
final build.

String progressive_web_app/icon_512x512

File path to the largest icon for this web application. If not defined,
defaults to the project icon.

Note: If the icon is not 512512, it will be automatically resized for the
final build.

String progressive_web_app/offline_page

The page to display, should the server hosting the page not be available. This
page is saved in the client's machine.

int progressive_web_app/orientation

The orientation to use when the web application is run through a mobile
device.

  * Any: No orientation is forced.

  * Landscape: Forces a horizontal layout (wider than it is taller).

  * Portrait: Forces a vertical layout (taller than it is wider).

bool variant/extensions_support

If `true` enables GDExtension support for this web build.

bool variant/thread_support

If `true`, the exported game will support threads. It requires a "cross-origin
isolated" website, which may be difficult to set up and is limited for
security reasons (such as not being able to communicate with third-party
websites).

If `false`, the exported game will not support threads. As a result, it is
more prone to performance and audio issues, but will only require to be run on
an HTTPS website.

bool vram_texture_compression/for_desktop

If `true`, allows textures to be optimized for desktop through the S3TC/BPTC
algorithm.

bool vram_texture_compression/for_mobile

If `true` allows textures to be optimized for mobile through the ETC2/ASTC
algorithm.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

