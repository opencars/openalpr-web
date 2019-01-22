[ci]: https://circleci.com/gh/shal/openalpr-web
[ci-badge]: https://circleci.com/gh/shal/openalpr-web.svg?style=svg

# Openalpr Web

[![Circle CI][ci-badge]][ci]

> :mag: Web service for car plates recognition

# Overview

Tiny micro-service responsible for car license plates recognition.

Thanks to [@openalpr](https://github.com/openalpr) for great [library](https://github.com/openalpr/openalpr).

## Documentation

Type: `GET`
Path: `/v2/identify/plate`

Parameters:
- `image_url` - Web URL of image to be analyzed.

```sh
$ curl -v http://localhost:8080/v2/identify/plate?image_url=https://images.spot.im/v1/production/fsrnogar718twyqmdqvf
```

# License

Project released under the terms of the [GNU Affero General Public License v3.0](./LICENSE).
