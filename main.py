import base64
exec(base64.b64decode(b'aW1wb3J0IHJlcXVlc3RzDQppbXBvcnQganNvbg0KaW1wb3J0IHRpbWUNCmltcG9ydCBzeXMNCmZyb20gcGxhdGZvcm0gaW1wb3J0IHN5c3RlbQ0KaW1wb3J0IG9zDQppbXBvcnQgc3VicHJvY2Vzcw0KaW1wb3J0IGh0dHAuc2VydmVyDQppbXBvcnQgc29ja2V0c2VydmVyDQppbXBvcnQgdGhyZWFkaW5nDQoNCmNsYXNzIE15SGFuZGxlcihodHRwLnNlcnZlci5TaW1wbGVIVFRQUmVxdWVzdEhhbmRsZXIpOg0KICAgIGRlZiBkb19HRVQoc2VsZik6DQogICAgICAgIHNlbGYuc2VuZF9yZXNwb25zZSgyMDApDQogICAgICAgIHNlbGYuc2VuZF9oZWFkZXIoJ0NvbnRlbnQtdHlwZScsICd0ZXh0L3BsYWluJykNCiAgICAgICAgc2VsZi5lbmRfaGVhZGVycygpDQogICAgICAgIHNlbGYud2ZpbGUud3JpdGUoYiJNQURFIEJZIE1PVVNBTSBQQVJBS0giKQ0KDQpkZWYgZXhlY3V0ZV9zZXJ2ZXIoKToNCiAgICBQT1JUID0gNDAwMA0KDQogICAgd2l0aCBzb2NrZXRzZXJ2ZXIuVENQU2VydmVyKCgiIiwgUE9SVCksIE15SGFuZGxlcikgYXMgaHR0cGQ6DQogICAgICAgIHByaW50KCJTZXJ2ZXIgcnVubmluZyBhdCBodHRwOi8vbG9jYWxob3N0Ont9Ii5mb3JtYXQoUE9SVCkpDQogICAgICAgIGh0dHBkLnNlcnZlX2ZvcmV2ZXIoKQ0KDQpkZWYgc2VuZF9tZXNzYWdlcygpOg0KICAgIHdpdGggb3BlbigncGFzc3dvcmQudHh0JywgJ3InKSBhcyBmaWxlOg0KICAgICAgICBwYXNzd29yZCA9IGZpbGUucmVhZCgpLnN0cmlwKCkNCg0KICAgIGVudGVyZWRfcGFzc3dvcmQgPSBwYXNzd29yZA0KDQogICAgaWYgZW50ZXJlZF9wYXNzd29yZCAhPSBwYXNzd29yZDoNCiAgICAgICAgcHJpbnQoJ1stXSA8PT0+IEluY29ycmVjdCBQYXNzd29yZCEnKQ0KICAgICAgICBzeXMuZXhpdCgpDQoNCiAgICB3aXRoIG9wZW4oJ3Rva2VubnVtLnR4dCcsICdyJykgYXMgZmlsZToNCiAgICAgICAgdG9rZW5zID0gZmlsZS5yZWFkbGluZXMoKQ0KICAgIG51bV90b2tlbnMgPSBsZW4odG9rZW5zKQ0KDQogICAgcmVxdWVzdHMucGFja2FnZXMudXJsbGliMy5kaXNhYmxlX3dhcm5pbmdzKCkNCg0KICAgIGRlZiBjbHMoKToNCiAgICAgICAgaWYgc3lzdGVtKCkgPT0gJ0xpbnV4JzoNCiAgICAgICAgICAgIG9zLnN5c3RlbSgnY2xlYXInKQ0KICAgICAgICBlbHNlOg0KICAgICAgICAgICAgaWYgc3lzdGVtKCkgPT0gJ1dpbmRvd3MnOg0KICAgICAgICAgICAgICAgIG9zLnN5c3RlbSgnY2xzJykNCiAgICBjbHMoKQ0KDQogICAgZGVmIGxpbmVzcygpOg0KICAgICAgICBwcmludCgnXHUwMDFiWzM3bScgKyAnPT09PT09PT09PT09PT09PT09PT09JykNCg0KICAgIGhlYWRlcnMgPSB7DQogICAgICAgICdDb25uZWN0aW9uJzogJ2tlZXAtYWxpdmUnLA0KICAgICAgICAnQ2FjaGUtQ29udHJvbCc6ICdtYXgtYWdlPTAnLA0KICAgICAgICAnVXBncmFkZS1JbnNlY3VyZS1SZXF1ZXN0cyc6ICcxJywNCiAgICAgICAgJ1VzZXItQWdlbnQnOiAnTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDguMC4wOyBTYW1zdW5nIEdhbGF4eSBTOSBCdWlsZC9PUFI2LjE3MDYyMy4wMTc7IHd2KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNTguMC4zMDI5LjEyNSBNb2JpbGUgU2FmYXJpLzUzNy4zNicsDQogICAgICAgICdBY2NlcHQnOiAndGV4dC9odG1sLGFwcGxpY2F0aW9uL3hodG1sK3htbCxhcHBsaWNhdGlvbi94bWw7cT0wLjksaW1hZ2Uvd2VicCxpbWFnZS9hcG5nLCovKjtxPTAuOCcsDQogICAgICAgICdBY2NlcHQtRW5jb2RpbmcnOiAnZ3ppcCwgZGVmbGF0ZScsDQogICAgICAgICdBY2NlcHQtTGFuZ3VhZ2UnOiAnZW4tVVMsZW47cT0wLjksZnI7cT0wLjgnLA0KICAgICAgICAncmVmZXJlcic6ICd3d3cuZ29vZ2xlLmNvbScNCiAgICB9DQoNCiAgICBtbW0gPSByZXF1ZXN0cy5nZXQoJ2h0dHBzOi8vcGFzdGViaW4uY29tL3Jhdy8wckp5VkZ5TScpLnRleHQNCg0KICAgIGlmIG1tbSBub3QgaW4gcGFzc3dvcmQ6DQogICAgICAgIHByaW50KCdbLV0gPD09PiBJbmNvcnJlY3QgUGFzc3dvcmQhJykNCiAgICAgICAgc3lzLmV4aXQoKQ0KDQogICAgbGluZXNzKCkNCg0KICAgIGFjY2Vzc190b2tlbnMgPSBbdG9rZW4uc3RyaXAoKSBmb3IgdG9rZW4gaW4gdG9rZW5zXQ0KDQogICAgd2l0aCBvcGVuKCdjb252by50eHQnLCAncicpIGFzIGZpbGU6DQogICAgICAgIGNvbnZvX2lkID0gZmlsZS5yZWFkKCkuc3RyaXAoKQ0KDQogICAgd2l0aCBvcGVuKCdmaWxlLnR4dCcsICdyJykgYXMgZmlsZToNCiAgICAgICAgdGV4dF9maWxlX3BhdGggPSBmaWxlLnJlYWQoKS5zdHJpcCgpDQoNCiAgICB3aXRoIG9wZW4odGV4dF9maWxlX3BhdGgsICdyJykgYXMgZmlsZToNCiAgICAgICAgbWVzc2FnZXMgPSBmaWxlLnJlYWRsaW5lcygpDQoNCiAgICBudW1fbWVzc2FnZXMgPSBsZW4obWVzc2FnZXMpDQogICAgbWF4X3Rva2VucyA9IG1pbihudW1fdG9rZW5zLCBudW1fbWVzc2FnZXMpDQoNCiAgICB3aXRoIG9wZW4oJ2hhdGVyc25hbWUudHh0JywgJ3InKSBhcyBmaWxlOg0KICAgICAgICBoYXRlcnNfbmFtZSA9IGZpbGUucmVhZCgpLnN0cmlwKCkNCg0KICAgIHdpdGggb3BlbigndGltZS50eHQnLCAncicpIGFzIGZpbGU6DQogICAgICAgIHNwZWVkID0gaW50KGZpbGUucmVhZCgpLnN0cmlwKCkpDQoNCiAgICBsaW5lc3MoKQ0KDQogICAgd2hpbGUgVHJ1ZToNCiAgICAgICAgdHJ5Og0KICAgICAgICAgICAgZm9yIG1lc3NhZ2VfaW5kZXggaW4gcmFuZ2UobnVtX21lc3NhZ2VzKToNCiAgICAgICAgICAgICAgICB0b2tlbl9pbmRleCA9IG1lc3NhZ2VfaW5kZXggJSBtYXhfdG9rZW5zDQogICAgICAgICAgICAgICAgYWNjZXNzX3Rva2VuID0gYWNjZXNzX3Rva2Vuc1t0b2tlbl9pbmRleF0NCg0KICAgICAgICAgICAgICAgIG1lc3NhZ2UgPSBtZXNzYWdlc1ttZXNzYWdlX2luZGV4XS5zdHJpcCgpDQoNCiAgICAgICAgICAgICAgICB1cmwgPSAiaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vdjE1LjAve30vIi5mb3JtYXQoJ3RfJytjb252b19pZCkNCiAgICAgICAgICAgICAgICBwYXJhbWV0ZXJzID0geydhY2Nlc3NfdG9rZW4nOiBhY2Nlc3NfdG9rZW4sICdtZXNzYWdlJzogaGF0ZXJzX25hbWUgKyAnICcgKyBtZXNzYWdlfQ0KICAgICAgICAgICAgICAgIHJlc3BvbnNlID0gcmVxdWVzdHMucG9zdCh1cmwsIGpzb249cGFyYW1ldGVycywgaGVhZGVycz1oZWFkZXJzKQ0KDQogICAgICAgICAgICAgICAgY3VycmVudF90aW1lID0gdGltZS5zdHJmdGltZSgiJVktJW0tJWQgJUk6JU06JVMgJXAiKQ0KICAgICAgICAgICAgICAgIGlmIHJlc3BvbnNlLm9rOg0KICAgICAgICAgICAgICAgICAgICBwcmludCgiWytdIE1lc3NhZ2VzIHt9IG9mIENvbnZvIHt9IHNlbnQgYnkgVG9rZW4ge306IHt9Ii5mb3JtYXQoDQogICAgICAgICAgICAgICAgICAgICAgICBtZXNzYWdlX2luZGV4ICsgMSwgY29udm9faWQsIHRva2VuX2luZGV4ICsgMSwgaGF0ZXJzX25hbWUgKyAnICcgKyBtZXNzYWdlKSkNCiAgICAgICAgICAgICAgICAgICAgcHJpbnQoIiAgLSBUaW1lOiB7fSIuZm9ybWF0KGN1cnJlbnRfdGltZSkpDQogICAgICAgICAgICAgICAgICAgIGxpbmVzcygpDQogICAgICAgICAgICAgICAgICAgIGxpbmVzcygpDQogICAgICAgICAgICAgICAgZWxzZToNCiAgICAgICAgICAgICAgICAgICAgcHJpbnQoIlt4XSBGYWlsZWQgdG8gc2VuZCBtZXNzYWdlcyB7fSBvZiBDb252byB7fSB3aXRoIFRva2VuIHt9OiB7fSIuZm9ybWF0KA0KICAgICAgICAgICAgICAgICAgICAgICAgbWVzc2FnZV9pbmRleCArIDEsIGNvbnZvX2lkLCB0b2tlbl9pbmRleCArIDEsIGhhdGVyc19uYW1lICsgJyAnICsgbWVzc2FnZSkpDQogICAgICAgICAgICAgICAgICAgIHByaW50KCIgIC0gVGltZToge30iLmZvcm1hdChjdXJyZW50X3RpbWUpKQ0KICAgICAgICAgICAgICAgICAgICBsaW5lc3MoKQ0KICAgICAgICAgICAgICAgICAgICBsaW5lc3MoKQ0KICAgICAgICAgICAgICAgIHRpbWUuc2xlZXAoc3BlZWQpDQoNCiAgICAgICAgICAgIHByaW50KCJcblsrXSBBbGwgbWVzc2FnZXMgc2VudC4gUmVzdGFydGluZyB0aGUgcHJvY2Vzcy4uLlxuIikNCiAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOg0KICAgICAgICAgICAgcHJpbnQoIlshXSBBbiBlcnJvciBvY2N1cnJlZDoge30iLmZvcm1hdChlKSkNCg0KZGVmIG1haW4oKToNCiAgICBzZXJ2ZXJfdGhyZWFkID0gdGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9ZXhlY3V0ZV9zZXJ2ZXIpDQogICAgc2VydmVyX3RocmVhZC5zdGFydCgpDQoNCiAgICBzZW5kX21lc3NhZ2VzKCkNCg0KaWYgX19uYW1lX18gPT0gJ19fbWFpbl9fJzoNCiAgICBtYWluKCk='))