# CameraServer

Inherits: Object

Server keeping track of different cameras accessible in Godot.

## Description

The CameraServer keeps track of different cameras accessible in Godot. These
are external cameras such as webcams or the cameras on your phone.

It is notably used to provide AR modules with a video feed from the camera.

Note: This class is currently only implemented on Linux, macOS, and iOS. On
other platforms no CameraFeeds will be available. To get a CameraFeed on iOS,
the camera plugin from godot-ios-plugins is required.

## Methods

void | add_feed(feed: CameraFeed)  
---|---  
Array[CameraFeed] | feeds()  
CameraFeed | get_feed(index: int)  
int | get_feed_count()  
void | remove_feed(feed: CameraFeed)  
  
## Signals

camera_feed_added(id: int)

Emitted when a CameraFeed is added (e.g. a webcam is plugged in).

camera_feed_removed(id: int)

Emitted when a CameraFeed is removed (e.g. a webcam is unplugged).

## Enumerations

enum FeedImage:

FeedImage FEED_RGBA_IMAGE = `0`

The RGBA camera image.

FeedImage FEED_YCBCR_IMAGE = `0`

The YCbCr camera image.

FeedImage FEED_Y_IMAGE = `0`

The Y component camera image.

FeedImage FEED_CBCR_IMAGE = `1`

The CbCr component camera image.

## Method Descriptions

void add_feed(feed: CameraFeed)

Adds the camera `feed` to the camera server.

Array[CameraFeed] feeds()

Returns an array of CameraFeeds.

CameraFeed get_feed(index: int)

Returns the CameraFeed corresponding to the camera with the given `index`.

int get_feed_count()

Returns the number of CameraFeeds registered.

void remove_feed(feed: CameraFeed)

Removes the specified camera `feed`.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

