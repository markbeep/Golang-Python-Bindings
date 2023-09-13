# Example on Golang bindings inside Python

Full article available on [https://markc.su](https://markc.su/posts/fusing-go-into-python/) or in the VIS Visionen.

To build the shared object file locally, run `make` or execute the specific build command:

```bash
go build -buildmode=c-shared -o library.so
```
