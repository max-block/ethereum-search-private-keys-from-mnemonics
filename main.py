from eth_account import Account

Account.enable_unaudited_hdwallet_features()


def read_mnemonics() -> list[str]:
    with open("./mnemonics.txt") as f:
        data = f.read()
    return [l.strip() for l in data.split("\n") if l.strip()]


def read_addresses() -> list[str]:
    with open("./addresses.txt") as f:
        data = f.read()
    return [l.strip().lower() for l in data.split("\n") if l.strip()]


def analyze_mnemonic(mnemonic: str, addresses: list[str]):
    for i in range(100):
        path = f"m/44'/60'/0'/0/{i}"
        acc = Account.from_mnemonic(mnemonic=mnemonic, account_path=path)
        address = acc.address.lower()
        if address in addresses:
            print(address, acc.privateKey.hex())


def main():
    addresses = read_addresses()
    for mnemonic in read_mnemonics():
        analyze_mnemonic(mnemonic, addresses)


if __name__ == "__main__":
    main()
