# tox-wiki

## Install and run
To install and run this little software you **must** type the following lines in a terminal.

```console
$ git clone git@github.com:SkyzohKeyx/tox-wiki.git && cd tox-wiki
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

When server run you can access it via [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Configuration
#### Introduction
tox-wiki is provided with a simple json config file (to change by yaml ?) that you **must** edit to make it works with your own repository.

Before doing anything, make sure that you have created an application for your repository.

You can create an application by replacing `YOUR_NAME` with your GitHub username/orgname and following this link: https://github.com/organizations/YOUR_NAME/settings/applications/new

#### Config.json
Basicaly the config.json file looks like this:
```json
{
  "github": {
    "client_id": "340769ec4bd82d0dc94a",
    "client_key": "5d1cc67a14b004b635f943f14723f996883e90d0",
    "repository": "ToxClient/wiki"
  }
}
```

| Key               | Usage                   | Description |
| :---------------- | :---------------------- | :---------- |
| github.client_id  | **Required** - Used to authentify you. | This is your GitHub app `client_id` |
| github.client_key | **Required** - Used to authentify you. | This is your GitHub app `client_secret` |
| github.repository | **Required** - Used to fetch the wiki files. | Must follow the format `USER_NAME/REPOSITORY_NAME` |
