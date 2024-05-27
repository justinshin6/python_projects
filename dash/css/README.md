# Dash CSS

### Overview 
[Link](https://dash.plotly.com/external-resources) to Documentation.

Create a folder named `assets` in the root of your app directory and include your CSS and JavaScript files in that folder. Dash automatically serves all the files that are included in this folder. By default, the URL to request the assets is /assets, but you can customize this with the assets_url_path argument to dash.Dash.

Important: If you're using Dash version 2.13 or earlier, you need to include __name__ in your Dash constructor when running these examples.

That is, `app = dash.Dash(__name__)` instead of `app = dash.Dash()`. Here's why.

If you are using Dash 2.14 or later, __name__ is no longer required.