SHELL := bash
DEPS := yq kubectl helm

all: check_deps deploy

check_deps:
	for dep in $(DEPS);do \
		which $$dep || echo "$$dep not found" | brew install $$dep ; \
	done


deploy:
	$(eval IMAGE_NAME := $(shell /bin/bash -c 'echo augury-$$RANDOM'))
	docker build -t ttl.sh/$(IMAGE_NAME):1h .
	docker push ttl.sh/$(IMAGE_NAME):1h
	yq -i '.image.name="ttl.sh/$(IMAGE_NAME)"' augury/values.yaml
	helm upgrade -i augury augury/