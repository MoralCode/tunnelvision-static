# TunnelVision (Static)

A reimplementation of TunnelVision as a statically-generated site.

## Tech Stack

Due to its use of Jinja2 templates and python base, Pelican seems like the best choice for static site generator here.

## How to Run

### Data
The data for this site exists in two primary folders:

#### `content/posts`
This is where the content and metadata for the entries themselves live.
They can be in any format that is supported by Pelican.

**Markdown**
```md

Title: Your title here
Id: <unique id here>
Date: 2026-02-06
Tags: a, b, c
Image: {photo}<directory for images within gallery>/<main image filename>
gallery: {photo}<directory for images within gallery>

<description or content here in markdown format>
```

**HTML**
This should work but is less tested
```html
<html>

<head>
	<title><!-- Your title here  --></title>
	<meta name="tags" content="thats, awesome" />
	<meta name="date" content="2012-07-09 22:28" />
	<meta name="image" content="{photo}<directory for images within gallery>/<main image filename>" />
	<meta name="gallery" content="{photo}<directory for images within gallery>" />

	<meta name="template" content="page" />
</head>

<body>
 <!-- description or content here in HTML format -->
</body>
</html>
```

**RST**
This should also work but is less tested and I don't feel like making an example for something that i don't use

#### `gallery`

The `gallery` directory is where the images are stored. This relies on a plugin to take the information in here and make it available to be generated into the page.

The gallery should contain subdirectories, one per entry in the posts section. This directory can be named pretty much whatever and can have the following contents:

| File      | Required | Purpose/Description      |
| --------- | ------------- | ------------- |
| <any image file, any name> | Yes, at least one | The image(s) that are part of this gallery |
| exif.txt  | No | Used to associate a string with each image, intended for author and image creation date but can be anything. The format of this file is specified in the [docs for the gallery plugin](https://github.com/pelican-plugins/photos?tab=readme-ov-file#exif-captions-and-blacklists)|
| captions.txt  | No | Used to associate a string with each image, intended for caption data (also used as alt text). The format of this file is specified in the [docs for the gallery plugin](https://github.com/pelican-plugins/photos?tab=readme-ov-file#exif-captions-and-blacklists)|


### Running for development

`uv run make devserver` will host a local dev server for you to browse with the contents generated from the site as-configured


## Lineage

This project is another major fork and large re-do of the [CampusPulse Access Directory](https://github.com/CampusPulse/access-directory) project, which itself is a major fork and rewrite of the original Database-backed [TunnelVision](https://github.com/wilsonmcdade/tunnelvision) codebase.


## Licensing

At the point of forking, neither CampusPulse Access had a license formally defined. All original/new code added here is licensed AGPL by default. A license should be added eventually once theres a clearer idea of how much of the base TunnelVision and CampusPulse Access projects are being used.
