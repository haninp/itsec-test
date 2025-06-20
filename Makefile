FILE ?= cybersecurity_attacks_fixed
PATH_VOL ?= ./soal1/file:/app/file

build_fixer:
	docker build \
		-f soal1/csv_newline_fixer/Dockerfile \
		--platform linux/arm64 \
		-t csv_newline_fixer:0 .

build_scoring:
	docker build \
		-f soal1/data_scoring/Dockerfile \
		--platform linux/arm64 \
		-t data_scoring:0 .

fix_csv:
	docker run --rm \
        -v "$(PATH_VOL)" \
        csv_newline_fixer:0 \
        file/$(FILE)_fixed.csv -y

scoring_completeness:
	docker run --rm \
		-v "$(PATH_VOL)" \
		data_scoring:0 \
		--dimension completeness.py \
		--input file/$(FILE).csv \
		--output file/$(FILE)_score_completeness.csv

scoring_validity:
	docker run --rm \
		-v "$(PATH_VOL)" \
		data_scoring:0 \
		--dimension validity.py \
		--input file/$(FILE).csv \
		--output file/$(FILE)_score_validity.csv

deduplication:
	docker run --rm \
		-v "./soal1/file:/app/file" \
		data_scoring:0 \
		--dimension uniqueness.py \
		--input file/cybersecurity_attacks_fixed.csv \
		--output file/cybersecurity_attacks_fixed_score_uniqueness.csv

update_rbl:
	docker run --rm \
		--entrypoint python \
		-v "$(PATH_VOL)" \
		data_scoring:0 \
		rbl_checker.py \
		--input file/$(FILE).csv

generate_dummy_rbl_cache:
	docker run --rm \
		--entrypoint python \
		-v "$(PATH_VOL)" \
		data_scoring:0 \
		dummy_rbl_cache.py \
		--input file/$(FILE).csv
		--blacklist-rate 0.05

qemu_installer:
	qemu-system-x86_64 \
		-m 1024 \
		-boot d \
		-cdrom soal2/gentoo-musl/iso/alpine-extended-3.19.1-x86_64.iso \
		-hda soal2/gentoo-musl/image/gentoo-musl.qcow2 \
		-net nic -net user \
		-nographic