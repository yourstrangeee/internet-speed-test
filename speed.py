import speedtest
import time

st = speedtest.Speedtest()

start = time.perf_counter()

print("=" * 55)
print("🚀               INTERNET SPEED TEST")
print("=" * 55)

print("\n[1/3] 🔍 Finding the best server...")
st.get_best_server()
server = st.results.server

print(f"✓ Connected to: {server.get('name', 'Unknown')} ({server.get('country', 'Unknown')})")

print("\n[2/3] ⬇️ Testing download speed...")
download = st.download()

print("\n[3/3] ⬆️ Testing upload speed...")
upload = st.upload()

ping = st.results.ping
end = time.perf_counter()

print("\n" + "=" * 55)
print("📊                 SPEED TEST RESULTS")
print("=" * 55)
print(f"📶 Ping             : {ping:.0f} ms")
print(f"⬇️ Download Speed   : {download / 1_000_000:.2f} Mbps")
print(f"⬆️ Upload Speed     : {upload / 1_000_000:.2f} Mbps")
print(f"⏱️ Time Taken       : {end - start:.2f} seconds")

print("\n🌍 Server Information")
print("-" * 55)

server_info = {
    "Name": server.get("name", "N/A"),
    "Country": server.get("country", "N/A"),
    "Sponsor": server.get("sponsor", "N/A"),
    "Latency": server.get("latency", "N/A"),
    "ID": server.get("id", "N/A"),
}

for key, value in server_info.items():
    print(f"{key:<10} : {value}")

print("=" * 55)
print("✅ Test Completed Successfully!")
print("=" * 55)