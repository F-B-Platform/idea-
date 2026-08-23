# Business Rules Consistency Checker
$targetDir = "d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai"
$files = Get-ChildItem -Path $targetDir -Filter "*.md" | Sort-Object Name

Write-Host "================================================================"
Write-Host "BUSINESS RULES CONSISTENCY AUDIT"
Write-Host "================================================================"

$rules = @(
    @{ Name = "Dine-In 2 Nhánh (VietQR trước / Tiền mặt sau)"; Regex = 'Dine-In|dine-in|Nhánh A|Nhánh B|prepaid|postpaid' },
    @{ Name = "Delivery 20k phí ship cố định, 100% VietQR, khóa COD"; Regex = '20\.000|20k|delivery_fee|Delivery' },
    @{ Name = "Takeaway POS 10 ly tặng 1 ly"; Regex = '10 ly|loyalty_cup|Takeaway|takeaway' },
    @{ Name = "Chấm công khóa WiFi Dual-Check (BSSID + Subnet IP)"; Regex = 'BSSID|bssid|subnet|Subnet|wifi-checkin' },
    @{ Name = "Loại bỏ Staff App / Thay bằng Web POS & KDS TV"; Regex = 'Web POS|KDS|Next\.js|Web PWA' },
    @{ Name = "Clean Architecture 4 lớp .NET 8"; Regex = 'Clean Architecture|Domain|Application|Infrastructure|WebAPI' },
    @{ Name = "5 Route Groups Next.js 14"; Regex = '\(customer\)|\(kds\)|\(staff\)|\(manager\)|\(admin\)' },
    @{ Name = "5 Docker Containers"; Regex = 'smartfb-postgres|smartfb-redis|smartfb-webapi|smartfb-frontend|smartfb-nginx' }
)

foreach ($r in $rules) {
    Write-Host "`n--- Rule: $($r.Name) ---"
    foreach ($f in $files) {
        $content = Get-Content $f.FullName -Raw -Encoding UTF8
        $match = $content -match $r.Regex
        Write-Host "  $($f.Name): $(if ($match) {'FOUND'} else {'NOT FOUND'})"
    }
}
