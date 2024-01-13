package main

import (
	"os"

	"github.com/taylormonacelli/hiscrime"
)

func main() {
	code := hiscrime.Execute()
	os.Exit(code)
}
